import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CsrfService {

  private baseURL = environment.backendURL;

  constructor(private http: HttpClient) { }

  get_csrf(){
    this.http.get(`${this.baseURL}/csrf`);
    console.log("CSRF")
  }
}
