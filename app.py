import random
from datetime import datetime

import streamlit as st

# ──────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NovaBank | Online Banking",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────────────────────────────────
# STYLING
# ──────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
        }

        #MainMenu, footer, header {visibility: hidden;}

        .stApp {
            background: radial-gradient(circle at 10% 0%, #1b1f3a 0%, #0d1024 45%, #05060f 100%);
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1100px;
        }

        /* Hero */
        .hero {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1.4rem 2rem;
            border-radius: 20px;
            background: linear-gradient(135deg, rgba(124,92,255,0.18), rgba(56,189,248,0.10));
            border: 1px solid rgba(255,255,255,0.08);
            margin-bottom: 1.6rem;
        }
        .hero h1 {
            font-size: 1.6rem;
            font-weight: 800;
            color: #f5f6ff;
            margin: 0;
            letter-spacing: -0.5px;
        }
        .hero span.brand-dot { color: #7c5cff; }
        .hero p {
            color: #a3a8c9;
            margin: 0.15rem 0 0 0;
            font-size: 0.88rem;
        }

        /* Generic glass card */
        .glass-card {
            background: rgba(255,255,255,0.045);
            border: 1px solid rgba(255,255,255,0.09);
            border-radius: 18px;
            padding: 1.6rem 1.8rem;
            backdrop-filter: blur(10px);
            margin-bottom: 1.2rem;
        }

        /* Balance card */
        .balance-card {
            background: linear-gradient(135deg, #6d3bff 0%, #4361ee 55%, #3a86ff 100%);
            border-radius: 22px;
            padding: 1.8rem 2rem;
            color: white;
            box-shadow: 0 20px 45px -18px rgba(72, 90, 255, 0.65);
            position: relative;
            overflow: hidden;
        }
        .balance-card::after {
            content: "";
            position: absolute;
            width: 220px; height: 220px;
            background: rgba(255,255,255,0.08);
            border-radius: 50%;
            top: -90px; right: -60px;
        }
        .balance-label {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            opacity: 0.85;
            margin-bottom: 0.3rem;
        }
        .balance-amount {
            font-family: 'JetBrains Mono', monospace;
            font-size: 2.4rem;
            font-weight: 700;
            letter-spacing: -1px;
        }
        .balance-sub {
            opacity: 0.85;
            font-size: 0.85rem;
            margin-top: 0.4rem;
        }

        /* Metric pill */
        .pill {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            background: rgba(124,92,255,0.15);
            border: 1px solid rgba(124,92,255,0.35);
            color: #c9bfff;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.3px;
        }

        /* Section headers */
        .section-title {
            color: #f0f1ff;
            font-weight: 700;
            font-size: 1.05rem;
            margin: 0 0 0.9rem 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        /* Transaction row */
        .txn-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.7rem 0.9rem;
            border-radius: 12px;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.06);
            margin-bottom: 0.5rem;
            font-size: 0.88rem;
            color: #d7d9f5;
        }
        .txn-row.credit { border-left: 3px solid #22c55e; }
        .txn-row.debit { border-left: 3px solid #f87171; }
        .txn-row.neutral { border-left: 3px solid #7c5cff; }

        /* Buttons */
        .stButton>button {
            border-radius: 12px !important;
            font-weight: 600 !important;
            border: none !important;
            padding: 0.55rem 1.2rem !important;
            background: linear-gradient(135deg, #7c5cff, #4361ee) !important;
            color: white !important;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }
        .stButton>button:hover {
            transform: translateY(-1px);
            box-shadow: 0 10px 25px -10px rgba(124,92,255,0.6);
        }

        /* Inputs */
        .stTextInput>div>div>input, .stNumberInput input {
            background: rgba(255,255,255,0.05) !important;
            border: 1px solid rgba(255,255,255,0.12) !important;
            border-radius: 10px !important;
            color: #f0f1ff !important;
        }

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] { gap: 6px; }
        .stTabs [data-baseweb="tab"] {
            background: rgba(255,255,255,0.04);
            border-radius: 10px;
            padding: 0.5rem 1rem;
            color: #a3a8c9;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #7c5cff, #4361ee) !important;
            color: white !important;
        }

        .id-chip {
            font-family: 'JetBrains Mono', monospace;
            background: rgba(34,197,94,0.12);
            border: 1px solid rgba(34,197,94,0.4);
            color: #86efac;
            padding: 0.5rem 0.9rem;
            border-radius: 10px;
            display: inline-block;
            font-weight: 700;
            letter-spacing: 1px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────────────────
# IN-MEMORY "DATABASE"  (mirrors data.py's account_records dict)
# ──────────────────────────────────────────────────────────────────────────
if "account_records" not in st.session_state:
    st.session_state.account_records = {}

if "session_id" not in st.session_state:
    st.session_state.session_id = None

if "flash" not in st.session_state:
    st.session_state.flash = None  # (type, message)

records = st.session_state.account_records


def flash(kind, msg):
    st.session_state.flash = (kind, msg)


def show_flash():
    if st.session_state.flash:
        kind, msg = st.session_state.flash
        getattr(st, kind)(msg)
        st.session_state.flash = None


def new_account_id():
    acc_id = str(random.randint(100000, 999999))
    while acc_id in records:
        acc_id = str(random.randint(100000, 999999))
    return acc_id


# ──────────────────────────────────────────────────────────────────────────
# HERO HEADER
# ──────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero">
        <div>
            <h1>🏦 Nova<span class="brand-dot">Bank</span></h1>
            <p>Fast, secure, no-nonsense online banking — built in Python & Streamlit.</p>
        </div>
        <div class="pill">● Demo Environment</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────────────────
# LOGGED-OUT VIEW: Create Account / Login
# ──────────────────────────────────────────────────────────────────────────
if st.session_state.session_id is None:
    show_flash()
    tab_login, tab_create = st.tabs(["🔐  Log In", "📝  Create Account"])

    with tab_login:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Welcome back</div>', unsafe_allow_html=True)
        with st.form("login_form"):
            acc_id = st.text_input("Account ID", max_chars=6, placeholder="e.g. 348213")
            pin = st.text_input("4-digit PIN", type="password", max_chars=4)
            submitted = st.form_submit_button("Log In", use_container_width=True)
        if submitted:
            if acc_id not in records:
                flash("error", "No matching account found.")
            elif records[acc_id]["pin"] != pin:
                flash("error", "Invalid PIN.")
            else:
                st.session_state.session_id = acc_id
                flash("success", f"Welcome back, {records[acc_id]['name']}!")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_create:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Open a new account</div>', unsafe_allow_html=True)
        with st.form("create_form"):
            name = st.text_input("Full name")
            mobile = st.text_input("10-digit mobile number", max_chars=10)
            pin1 = st.text_input("Set a 4-digit PIN", type="password", max_chars=4)
            pin2 = st.text_input("Confirm PIN", type="password", max_chars=4)
            submitted_c = st.form_submit_button("Create Account", use_container_width=True)
        if submitted_c:
            if len(name.strip()) == 0:
                flash("error", "Name cannot be empty.")
            elif not (mobile.isdigit() and len(mobile) == 10):
                flash("error", "Mobile number must contain exactly 10 digits.")
            elif not (pin1.isdigit() and len(pin1) == 4):
                flash("error", "PIN must be exactly 4 digits.")
            elif pin1 != pin2:
                flash("error", "PINs do not match.")
            else:
                acc_id = new_account_id()
                records[acc_id] = {
                    "name": name.strip(),
                    "phone": mobile,
                    "pin": pin1,
                    "balance": 0.0,
                    "history": [],
                }
                flash("success", f"Account created! Your Account ID is **{acc_id}** — save it, you'll need it to log in.")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────
# LOGGED-IN VIEW: Dashboard
# ──────────────────────────────────────────────────────────────────────────
else:
    acc_id = st.session_state.session_id
    acct = records[acc_id]

    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown(
            f"""
            <div class="balance-card">
                <div class="balance-label">Available Balance</div>
                <div class="balance-amount">₹{acct['balance']:,.2f}</div>
                <div class="balance-sub">{acct['name']} · Account ID <span class="id-chip">{acc_id}</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with top_r:
        st.write("")
        st.write("")
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.session_id = None
            flash("info", "Logged out.")
            st.rerun()

    st.write("")
    show_flash()

    tabs = st.tabs(["💰 Deposit", "💸 Withdraw", "🔁 Transfer", "🧾 Statement", "🔑 Change PIN"])

    # ---- Deposit ----
    with tabs[0]:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Deposit funds</div>', unsafe_allow_html=True)
        with st.form("deposit_form"):
            amt = st.number_input("Amount (₹)", min_value=0.0, step=100.0, format="%.2f")
            dep_submit = st.form_submit_button("Deposit", use_container_width=True)
        if dep_submit:
            if amt <= 0:
                flash("error", "Amount must be higher than 0.")
            else:
                acct["balance"] += amt
                ts = datetime.now().strftime("%Y/%m/%d %H:%M")
                acct["history"].append(("credit", f"[{ts}] Credit: +₹{amt:,.2f}"))
                flash("success", f"Added ₹{amt:,.2f}. New balance: ₹{acct['balance']:,.2f}")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ---- Withdraw ----
    with tabs[1]:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Withdraw funds</div>', unsafe_allow_html=True)
        with st.form("withdraw_form"):
            amt_w = st.number_input("Amount (₹)", min_value=0.0, step=100.0, format="%.2f", key="wd_amt")
            wd_submit = st.form_submit_button("Withdraw", use_container_width=True)
        if wd_submit:
            if amt_w <= 0:
                flash("error", "Amount must be greater than 0.")
            elif acct["balance"] < amt_w:
                flash("error", "Insufficient funds.")
            else:
                acct["balance"] -= amt_w
                ts = datetime.now().strftime("%Y/%m/%d %H:%M")
                acct["history"].append(("debit", f"[{ts}] Debit: -₹{amt_w:,.2f}"))
                flash("success", f"Withdrew ₹{amt_w:,.2f}. Remaining balance: ₹{acct['balance']:,.2f}")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ---- Transfer ----
    with tabs[2]:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Send money</div>', unsafe_allow_html=True)
        with st.form("transfer_form"):
            target = st.text_input("Recipient Account ID", max_chars=6)
            amt_t = st.number_input("Amount (₹)", min_value=0.0, step=100.0, format="%.2f", key="tr_amt")
            tr_submit = st.form_submit_button("Send", use_container_width=True)
        if tr_submit:
            if target not in records:
                flash("error", "Recipient ID not found.")
            elif target == acc_id:
                flash("error", "Self-transfers are not allowed.")
            elif amt_t <= 0:
                flash("error", "Invalid amount.")
            elif acct["balance"] < amt_t:
                flash("error", "Transfer failed: insufficient balance.")
            else:
                acct["balance"] -= amt_t
                records[target]["balance"] += amt_t
                ts = datetime.now().strftime("%Y/%m/%d %H:%M")
                acct["history"].append(("debit", f"[{ts}] Sent ₹{amt_t:,.2f} to ID {target}"))
                records[target]["history"].append(("credit", f"[{ts}] Recv ₹{amt_t:,.2f} from ID {acc_id}"))
                flash("success", f"₹{amt_t:,.2f} sent to {target}.")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ---- Statement ----
    with tabs[3]:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Mini statement</div>', unsafe_allow_html=True)
        if not acct["history"]:
            st.info("No transactions on record yet.")
        else:
            for kind, entry in reversed(acct["history"]):
                st.markdown(f'<div class="txn-row {kind}">{entry}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ---- Change PIN ----
    with tabs[4]:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Update your PIN</div>', unsafe_allow_html=True)
        with st.form("pin_form"):
            cur = st.text_input("Current PIN", type="password", max_chars=4)
            newp = st.text_input("New 4-digit PIN", type="password", max_chars=4)
            conf = st.text_input("Confirm new PIN", type="password", max_chars=4)
            pin_submit = st.form_submit_button("Update PIN", use_container_width=True)
        if pin_submit:
            if acct["pin"] != cur:
                flash("error", "Wrong current PIN.")
            elif not (newp.isdigit() and len(newp) == 4):
                flash("error", "New PIN must be exactly 4 digits.")
            elif newp != conf:
                flash("error", "PINs do not match.")
            else:
                acct["pin"] = newp
                flash("success", "PIN changed successfully.")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align:center; color:#5b5f82; font-size:0.78rem; margin-top:2rem;">
        NovaBank demo · data is stored in-memory for this session only, not a real bank.
    </div>
    """,
    unsafe_allow_html=True,
)
