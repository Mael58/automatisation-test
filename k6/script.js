import { Client, StatusOK } from 'k6/net/grpc';
import { check, sleep } from 'k6';

export const options = {
  executor: 'ramping-vus',
  startVUs: 0,
  stages: [
    { target: 10, duration: '20s'},
    { target: 15, duration: '10s' },
    { target: 0, duration: '10s' },
  ]
};

const client = new Client();
client.load(['definitions'], 'payment.proto');

export default () => {
  client.connect('172.17.0.1:50051', {plaintext: true});

  const data = { 
    card_number: 129,
    event_id: 1,
    user_id: 90,
    amount: 200.0
   };
  const response = client.invoke('Payment/Pay', data);

  check(response, {
    'status is OK': (r) => r && r.status === StatusOK,
  });

  check(response, {
    'status payment is OK': (r) => r.message['status']
  })

  client.close();
  sleep(10);
};