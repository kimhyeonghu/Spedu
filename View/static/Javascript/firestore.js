// Import the functions you need from the SDKs you need

const firebaseConfig = {
  apiKey: "AIzaSyAhONsOYfqp3ox_L5bCy0cpX_f-iQxdc9I",
  authDomain: "spedu-3fd4f.firebaseapp.com",
  databaseURL: "https://spedu-3fd4f-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "spedu-3fd4f",
  storageBucket: "spedu-3fd4f.appspot.com",
  messagingSenderId: "297243626132",
  appId: "1:297243626132:web:129e6edfab962e5ab24281"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
var db = firebase.firestore();
