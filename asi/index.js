const input = require("readline-sync")
const express = require("express");
const app = express();

const firebase = require('firebase-admin');
const serviceAccount = require("./asi-act-firebase-adminsdk-rgmzt-3576e13192.json");

const firebaseConfig = {
  credential: firebase.credential.cert(serviceAccount),
  apiKey: "AIzaSyCje8xD-O4v30DS69dCgdyeX1nZ5JIbhmY",
  authDomain: "asi-act.firebaseapp.com",
  projectId: "asi-act",
  databaseURL: "https://asi-act-default-rtdb.firebaseio.com/",
  storageBucket: "asi-act.appspot.com",
  messagingSenderId: "206726379771",
  appId: "1:206726379771:web:c80e476afcbc89fa87185e",
  measurementId: "G-K8VMBVREXB"
};

firebase.initializeApp(firebaseConfig);

const ref = firebase.app().database().ref("student/");


function create(){
    var student_id = input.question("Student ID: ");
    var first_name = input.question("First name: ");
    var last_name = input.question("Last name: ");
    var section = input.question("Section: ");

    const student = ref.child(student_id);

    student.set({
        student_id: student_id,
        first_name: first_name,
        last_name: last_name,
        section: section
    });
}

ref.on("value", function(data){
    console.log(data.val());
});

function update(){
    var id = input.question("Student ID: ");
    console.log("Choose what you want to update: ");
    console.log("[1] First Name ");
    console.log("[2] Last Name ");
    console.log("[3] Section ");
    var opt = input.question("Option: ");

    if (opt == 1){
        var upref = firebase.app().database().ref("student/"+id);
        var fname = input.question("Enter first name: ");

        upref.update({
            first_name: fname
        })
    }

    else if (opt == 2){
        var upref = firebase.app().database().ref("student/"+id);
        var lname = input.question("Enter last name: ");

        upref.update({
            last_name: lname
        })
    }

    else if (opt == 3){
        var upref = firebase.app().database().ref("student/"+id);
        var section = input.question("Enter section: ");

        upref.update({
            section: section
        })
    }

    else{
        console.log("OPTION DOES NOT EXIST!")
    }
}

update()





