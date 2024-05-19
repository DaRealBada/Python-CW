import subscriptionManager as SM
from database import *
import feedbackManager as FM

def check_subscription_status():    
    customer_ID = input("What is the customer's ID?: ")
    sub_status = SM.check_subscription(customer_ID, SM.load_subscriptions())
    # load_subscriptions to check the subscription status
    if sub_status == True:
        print(f"Customer with ID {customer_ID} has an active subscription")
    else:
        print("ERROR: Subscription status is inactive")

