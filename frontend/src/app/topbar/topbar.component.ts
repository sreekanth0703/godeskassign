import { Component, OnInit } from '@angular/core';
import {ConfigService} from '../config.service';

@Component({
  selector: 'app-topbar',
  templateUrl: './topbar.component.html',
  styleUrls: ['./topbar.component.css']
})
export class TopbarComponent implements OnInit {

  constructor(
    private config: ConfigService
  ) { }

  logout(): void {
    let response_data = this.config.Request('user_logout/', 'get');
    response_data.subscribe(
              res_data => {
                console.log("success!", res_data);
                window.location.href = 'login/';
              },
              error => {
                console.log("couldn't post because", error);
              }
          );
  }

  ngOnInit(): void {
  }

}
