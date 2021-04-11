import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { map } from "rxjs/operators";
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {

  configUrl = 'http://localhost:8000/api/'
  constructor(
    private http: HttpClient
  ) { }


  Request(url:string, method='get', data={}, pk=0) {
    if(method == 'post'){
      return this.http.post(this.configUrl+url, data,  {withCredentials: true});
    }
    if(method == 'put'){
      return this.http.put(this.configUrl+url+pk+'/', data,  {withCredentials: true});
    }
    else if(method=='delete'){
      return this.http.delete(this.configUrl+url+pk, {withCredentials: true});
    }
    else {
      return this.http.get(this.configUrl+url, {withCredentials: true});
    }
  }
}
