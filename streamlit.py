import streamlit as st
from bankmanagement import Bank

bank = Bank()

st.set_page_config(page_title="Bank Management System", page_icon="🏦")

st.title(" Bank Management System")

menu = st.sidebar.selectbox(
    "Select",
    [ 
        "Create Account",
        "Deposit",
        "Withdraw",
        "Show Details",
        "Update Details",
        "Delete Account"
    ]
)



if menu == "Create Account":

    st.header("Create Account")

    name = st.text_input("Name")

    age = int(st.number_input("Age", min_value=18, max_value=100))

    email = st.text_input("Email")

    pin = st.text_input("5 Digit PIN", type="password")

    if st.button("Create"):

        success, msg = bank.create_account(
            name,
            age,
            email,
            pin
        )

        if success:
            st.success("Account Created Successfully")
            st.write(msg)
        else:
            st.error(msg)



elif menu == "Deposit":

    st.header("Deposit Money")

    acc = st.text_input("Account Number")

    pin = st.text_input("PIN", type="password")

    amount = float(st.number_input("Amount", min_value=1.0))

    if st.button("Deposit"):

        success, msg = bank.deposit(acc, pin, amount)

        if success:
            st.success(msg)
        else:
            st.error(msg)



elif menu == "Withdraw":

    st.header("Withdraw Money")

    acc = st.text_input("Account Number")

    pin = st.text_input("PIN", type="password")

    amount = float(st.number_input("Amount", min_value=1.0))

    if st.button("Withdraw"):

        success, msg = bank.withdraw(acc, pin, amount)

        if success:
            st.success(msg)
        else:
            st.error(msg)



elif menu == "Show Details":

    st.header("Show Details")

    acc = st.text_input("Account Number")

    pin = st.text_input("PIN", type="password")

    if st.button("Show"):

        user = bank.login(acc, pin)

        if user:
            st.json(user)
        else:
            st.error("Invalid Credentials")



elif menu == "Update Details":

    st.header("Update Details")

    acc = st.text_input("Account Number")

    pin = st.text_input("PIN", type="password")

    name = st.text_input("New Name")

    email = st.text_input("New Email")

    if st.button("Update"):

        success, msg = bank.update_details(
            acc,
            pin,
            name,
            email
        )

        if success:
            st.success(msg)
        else:
            st.error(msg)



elif menu == "Delete Account":

    st.header("Delete Account")

    acc = st.text_input("Account Number")

    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):

        success, msg = bank.delete_account(acc, pin)

        if success:
            st.success(msg)
        else:
            st.error(msg)
