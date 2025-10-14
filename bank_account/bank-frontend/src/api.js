
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const api = {
  getAccounts: () => axios.get(`${BASE_URL}/accounts`),

  createAccount: (data) =>
    axios.post(`${BASE_URL}/create-account`, {
      first_name: data.first_name,
      last_name: data.last_name,
      address: data.address,
      email: data.email,
      phone_number: data.phone_number,
      nin: data.nin,
      bvn: data.bvn,
    }),


  deposit: (account_number, amount) =>
    axios.post(`${BASE_URL}/deposit/${account_number}`, { amount }),

  withdraw: (account_number, amount) =>
    axios.post(`${BASE_URL}/withdraw/${account_number}`, { amount }),

 
  transfer: (sender, receiver, amount) =>
    axios.post(`${BASE_URL}/transfer`, {
      sender_account_number: sender,
      receiver_account_number: receiver,
      amount,
    }),

  signUp: (data) => axios.post(`${BASE_URL}/create-account`, data),
  login: (data) => axios.post(`${BASE_URL}/login`, data),

};

export default api;
