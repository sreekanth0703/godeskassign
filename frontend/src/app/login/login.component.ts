import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';
import {ConfigService} from '../config.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginForm = new FormGroup({
    username: new FormControl(''),
    password: new FormControl(''),
  });

  constructor(
    private formBuilder: FormBuilder,
    private config: ConfigService
  ) { }

  login(): void {
    var data = JSON.stringify(this.loginForm.getRawValue());
    let response_data = this.config.Request('user_login/', 'post', data);
    response_data.subscribe(
              res_data => {
                console.log("success!", res_data);
                window.location.href='';
              },
              error => {
                console.log("couldn't post because", error);
                alert("Invalid Credentials");
              }
          );
    this.loginForm.reset();
  }

  ngOnInit(): void {
  }

}
