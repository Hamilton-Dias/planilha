import pandas as pd

def process_csv(file_path):
    df = _load_to_memory(file_path)
    df = _prepare_df(df)
    mrr_dict = _generate_mrr_dict(df)
    churn_dict = _generate_churn_dict(df)

    return {'mrr': mrr_dict, 'churns': churn_dict}

def _load_to_memory(file_path):
    # Ler o arquivo CSV ou Excel
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Formato de arquivo não suportado. Apenas CSV ou Excel (xlsx) são suportados.")
    
    return df

def _prepare_df(df):
    df.rename(columns={
        'quantidade cobranças': 'billing_count',
        'cobrada a cada X dias': 'billing_frequency',
        'data início': 'start_date',
        'status': 'subscription_status',
        'data status': 'status_date',
        'data cancelamento': 'cancel_date',
        'valor': 'amount',
        'próximo ciclo': 'next_billing_date',
        'ID assinante': 'subscriber_id'
    }, inplace=True)

    df['start_date'] = pd.to_datetime(df['start_date'])
    df['status_date'] = pd.to_datetime(df['status_date'])
    df['cancel_date'] = pd.to_datetime(df['cancel_date'])

    df['month_year'] = df['start_date'].dt.to_period('M')

    return df

def _generate_mrr_dict(df):
    active_or_cancelled_subscriptions = df[(df['subscription_status'] == 'Ativa') | ((df['subscription_status'] == 'Cancelada') & (df['cancel_date'] >= df['month_year'].dt.end_time))]

    mrr_data = active_or_cancelled_subscriptions.groupby('month_year')['amount'].sum().reset_index(name='mrr')
    mrr_data['mrr'] = round(mrr_data['mrr'], 2)
    mrr_data['month_year'] = mrr_data['month_year'].astype(str)

    mrr_dict = mrr_data.set_index('month_year').to_dict()['mrr']

    return mrr_dict

def _generate_churn_dict(df):
    active_or_cancelled_subscriptions = df[(df['subscription_status'] == 'Ativa') | ((df['subscription_status'] == 'Cancelada') & (df['cancel_date'] >= df['month_year'].dt.end_time))]
    active_subscriptions = active_or_cancelled_subscriptions[active_or_cancelled_subscriptions['subscription_status'] == 'Ativa'].groupby('month_year').size().reset_index(name='active_subscriptions')
    cancelled_subscriptions = active_or_cancelled_subscriptions[active_or_cancelled_subscriptions['subscription_status'] == 'Cancelada'].groupby('month_year').size().reset_index(name='cancelled_subscriptions')

    churn_data = pd.merge(active_subscriptions, cancelled_subscriptions, on='month_year', how='outer')
    churn_data['churn_rate'] = (churn_data['cancelled_subscriptions'] / (churn_data['active_subscriptions'] + churn_data['cancelled_subscriptions'])) * 100
    churn_data['churn_rate'] = churn_data['churn_rate'].round(2)
    churn_data.fillna(0, inplace=True)
    churn_data['month_year'] = churn_data['month_year'].astype(str)

    churn_dict = churn_data.set_index('month_year').to_dict()['churn_rate']

    return churn_dict