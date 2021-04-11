import { Component, OnInit } from '@angular/core';
import {ConfigService} from '../config.service';
import { map } from "rxjs/operators";


@Component({
  selector: 'app-mainpage',
  templateUrl: './mainpage.component.html',
  styleUrls: ['./mainpage.component.css']
})
export class MainpageComponent implements OnInit {

  constructor(
    private config: ConfigService
  ) { }

  user_info: any;
  login_check(): void {
    let response_data = this.config.Request('status/', 'post');
    response_data.subscribe(
              res_data => {
                console.log("success!", res_data);
                this.user_info = res_data;
              },
              error => {
                console.log("couldn't post because", error);
                window.location.href='login/';
              }
          );
  }

  ngOnInit(): void {
    this.login_check();
  }

}
