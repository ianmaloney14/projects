// In browsers, use a <script> tag. In Node.js, uncomment the following line:
const xrpl = require("xrpl");

// Wrap code in an async function so we can use await
async function main() {
  // Define the network client
  const client = new xrpl.Client("wss://s.altnet.rippletest.net:51233");
  await client.connect();

  // ... custom code goes here

  // Disconnect when done (If you omit this, Node.js won't end the process)
  client.disconnect();
}

main();

// CREATE WALLET
async function createWallet() {
  const api = new xrpl.Client("wss://s.altnet.rippletest.net:51233");

  await api.connect();

  const wallet = xrpl.Wallet.generate();

  console.log(wallet);

  api.disconnect();
}

createWallet();

// FUND WALLET
async function fundWallet() {
  const api = new xrpl.Client("wss://s.altnet.rippletest.net:51233");

  await api.connect();

  const wallet = await api.fundWallet();

  console.log(wallet);

  api.disconnect();
}

fundWallet();

// SEND XRP
async function sendXRP() {
  const api = new xrpl.Client("wss://s.altnet.rippletest.net:51233");

  await api.connect();

  const walletObject = await api.fundWallet();
  const walletObject2 = await api.fundWallet();

  const wallet = walletObject.wallet;

  const preparedTransaction = await api.autofill({
    TransactionType: "Payment",
    Account: wallet.classicAddress,
    Amount: xrpl.xrpToDrops("1"),
    Destination: walletObject2.wallet.classicAddress,
  });
  //SIGN TRANSACTION
  const signed = wallet.sign(preparedTransaction);

  const results = await api.submitAndWait(signed.tx_blob);

  console.log(results);

  api.disconnect();
}

sendXRP();
