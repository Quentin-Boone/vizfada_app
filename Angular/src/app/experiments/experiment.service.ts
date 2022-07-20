import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { DataJSON, Folder } from '../utils/text-url';



@Injectable({
  providedIn: 'root'
})
export class ExperimentService {
  
  private backendURL = environment.backendURL;

  constructor(private http: HttpClient) { }
  
  get_experiment(id): Observable<(DataJSON | Folder)[]> {
    let url = `${this.backendURL}/experiment/${id}`;
    console.log("Fetching experiment at ", url);
    return this.http.get<(DataJSON | Folder)[]>(`${url}`, {responseType: 'json', reportProgress: true, withCredentials: true});
  }

}
