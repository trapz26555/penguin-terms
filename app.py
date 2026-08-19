from flask import Flask

app = Flask(__name__)

# Rebranded from the Tedbot terms page style — swap colors, wording, and
# sections however you want. The important part is that this route returns
# HTML at a public URL you can put in your bot's profile / Developer Portal
# "Terms of Service URL" field.
TERMS_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Penguin Eats — Terms &amp; Refund Policy</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  :root {
    --bg: #0a0e12;
    --card: #12171c;
    --card-border: #1f262d;
    --accent: #2dd4bf;
    --text: #f2f5f4;
    --text-dim: #9aa5ab;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 56px 20px 80px;
    background: var(--bg);
    color: var(--text);
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    line-height: 1.6;
  }
  .wrap { max-width: 720px; margin: 0 auto; }
  h1 {
    font-size: 40px;
    font-weight: 800;
    margin: 0 0 16px;
    background: linear-gradient(90deg, #ffffff 0%, var(--accent) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .intro { color: var(--text-dim); font-size: 16px; max-width: 560px; margin-bottom: 8px; }
  .updated { color: #5b6670; font-size: 13px; margin-bottom: 32px; }

  .summary {
    background: var(--card);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 22px 24px;
    margin-bottom: 28px;
    display: flex;
    gap: 14px;
  }
  .summary .icon { font-size: 20px; line-height: 1.4; }
  .summary-label {
    color: var(--accent);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 6px;
  }
  .summary p { margin: 0; color: var(--text); }

  .section {
    background: var(--card);
    border: 1px solid var(--card-border);
    border-left: 3px solid var(--accent);
    border-radius: 10px;
    padding: 24px 26px;
    margin-bottom: 20px;
  }
  .section-head {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 16px;
  }
  .section-num { color: #5b6670; font-size: 13px; font-weight: 700; }
  .section-icon { font-size: 18px; }
  .section-title {
    color: var(--accent);
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
  .section p { color: var(--text); margin: 0 0 12px; }
  .section p:last-child { margin-bottom: 0; }

  .check-item {
    display: flex;
    align-items: center;
    gap: 12px;
    background: #171d23;
    border-radius: 8px;
    padding: 14px 16px;
    margin-bottom: 10px;
    color: var(--text);
  }
  .check-item .tick {
    flex-shrink: 0;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: var(--accent);
    color: #0a0e12;
    font-size: 12px;
    font-weight: 900;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .subgrid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 16px;
  }
  @media (max-width: 560px) { .subgrid { grid-template-columns: 1fr; } }
  .subcard {
    background: #171d23;
    border-radius: 8px;
    padding: 18px 20px;
  }
  .subcard .icon { font-size: 18px; margin-bottom: 10px; }
  .subcard .title { font-weight: 700; margin-bottom: 6px; }
  .subcard .desc { color: var(--text-dim); font-size: 14px; margin: 0; }

  footer {
    margin-top: 40px;
    padding-top: 24px;
    border-top: 1px solid var(--card-border);
    text-align: center;
  }
  footer .brand {
    color: var(--accent);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.1em;
  }
  footer .brand::before {
    content: "● ";
  }
</style>
</head>
<body>
  <div class="wrap">
    <h1>Terms &amp; Refund Policy</h1>
    <p class="intro">The rules of the road for every order. Please read before you
      pay — completing a payment means you agree to these terms.</p>
    <div class="updated">Last updated August 2026</div>

    <div class="summary">
      <div class="icon">💡</div>
      <div>
        <div class="summary-label">The short version</div>
        <p>Pay securely by Venmo, PayPal, Zelle, Cash App, or Chime.
          <strong>Refunds only happen if an order is cancelled or can't be
          completed</strong> — otherwise payments are final. Don't file false
          chargebacks. Questions? Ask your seller first.</p>
      </div>
    </div>

    <div class="section">
      <div class="section-head">
        <span class="section-num">01</span>
        <span class="section-icon">💵</span>
        <span class="section-title">Refund Policy</span>
      </div>
      <p><strong>Refunds are only issued if:</strong></p>
      <div class="check-item"><span class="tick">✓</span> The order was <strong>cancelled</strong> before it was fulfilled, or</div>
      <div class="check-item"><span class="tick">✓</span> You were <strong>unable to complete or receive</strong> the order on our end.</div>
      <p>Outside of these cases, <strong>payments are final</strong>. No refunds for a change of mind once an order is in progress or delivered.</p>
    </div>

    <div class="section">
      <div class="section-head">
        <span class="section-num">02</span>
        <span class="section-icon">💳</span>
        <span class="section-title">Payment Processing</span>
      </div>
      <p>Payments are sent directly to the seller via <strong>Venmo, PayPal, Zelle, Cash App, or Chime</strong>. We never handle or store your card or banking details.</p>
      <div class="subgrid">
        <div class="subcard">
          <div class="icon">⏱️</div>
          <div class="title">Payment expiry</div>
          <p class="desc">Payment requests expire after a short window. Just ask for a new one if yours lapses.</p>
        </div>
        <div class="subcard">
          <div class="icon">🔒</div>
          <div class="title">Pay who you trust</div>
          <p class="desc">Payments go straight to the seller through their own payment app.</p>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-head">
        <span class="section-num">03</span>
        <span class="section-icon">⚠️</span>
        <span class="section-title">Disputes &amp; Chargebacks</span>
      </div>
      <p>Filing a chargeback or fraud claim on a legitimate, fulfilled order is itself fraud and will be contested. <strong>Accounts found to be fraudulent may be permanently denied future service.</strong></p>
    </div>

    <div class="section">
      <div class="section-head">
        <span class="section-num">04</span>
        <span class="section-icon">💬</span>
        <span class="section-title">Questions</span>
      </div>
      <p>Have a question about a charge or need to discuss a refund? <strong>Reach out to the seller you ordered from</strong> before paying or filing any dispute — they're the best resource for anything order-specific.</p>
    </div>

    <footer>
      <span class="brand">PENGUIN EATS</span>
    </footer>
  </div>
</body>
</html>
"""


@app.route("/terms")
def terms():
    return TERMS_HTML


@app.route("/")
def home():
    return '<p style="font-family:sans-serif">Penguin Eats bot service. See <a href="/terms">/terms</a>.</p>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
