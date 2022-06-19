import streamlit as st
import streamlit.components.v1 as components

st.image("a123.png")
st.title("项目介绍：我，盘子，打钱！")
body = """
       <!DOCTYPE html>
<html lang="en">
<body>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
    integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
    crossorigin="anonymous"></script>
<button class="enableEthereumButton btn">Connect wallet</button>
<button class="sendEthButton btn">Join in Web4</button>
</body>
<script>
const ethereumButton = document.querySelector('.enableEthereumButton');
const sendEthButton = document.querySelector('.sendEthButton');
let accounts = [];
//Sending Ethereum to an address
sendEthButton.addEventListener('click', () => {
  window.parent.ethereum
    .request({
      method: 'eth_sendTransaction',
      params: [
        {
          from: accounts[0],
          to: '0xDeE245EbB9C4A9553CE1579b7412Eb6E223daAA3',
          value: '0x2386f26fc10000',
        },
      ],
    })
    .then((txHash) => console.log(txHash))
    .catch((error) => console.error);
});

ethereumButton.addEventListener('click', () => {
  getAccount();
});

async function getAccount() {
  accounts = await window.parent.ethereum.request({ method: 'eth_requestAccounts' });
}
  </script>
</html>
        """

components.html(body,height=200,)
#window.parent
