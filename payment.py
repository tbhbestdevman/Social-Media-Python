```python
import stripe
from database import database_connection
from user import current_user

stripe.api_key = app_config['STRIPE_SECRET_KEY']

def make_payment(amount, currency, source, description):
    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            source=source,
            description=description,
        )
        save_payment_to_db(charge)
        return True
    except stripe.error.StripeError as e:
        print(e)
        return False

def save_payment_to_db(charge):
    payment_data = {
        'user_id': current_user.id,
        'amount': charge.amount,
        'currency': charge.currency,
        'description': charge.description,
        'status': charge.status,
    }
    database_connection.insert('payments', payment_data)
```