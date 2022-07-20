import { HttpClient, HttpXsrfTokenExtractor } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { environment } from '../../environments/environment';
import { Fields } from "../utils/metadata";
import { CookieService } from 'ngx-cookie-service';


@Injectable({
  providedIn: 'root',
})
export class DataService {

  private baseURL = environment.backendURL;
  public submittedData = new Subject;

  constructor(private http: HttpClient, private cookieService: CookieService) {
  }

  build_url(uri: string, data?: Object): string {
    let url = `${this.baseURL}/${uri}`;
    if (typeof data !== "undefined") {
      url = url + `/?q=${JSON.stringify(data)}`;
    }
    return url;
  }

  post_blob(type: string, data: Object): Observable<Blob> {
    let url: string = "";
    switch (type) {
      case 'heatmap':
        url = `${this.baseURL}/heatmap/img/`;
        break;
      default:
        throw new Error("Invalid parameter: type must be 'heatmap', not " + type);
    }
    console.log("Fetching blob for ", type, " at ", url);
    return this.http.post(`${url}`, data, { responseType: 'blob', reportProgress: true, withCredentials: true });
  }

  post_json(type: string, data?: Object): Observable<Object> {
    let url: string = "";
    switch (type) {
      case 'plotly':
        url = `${this.baseURL}heatmap/plotly/`;
        break;
      default:
        throw new Error("Invalid parameter: type must be 'plotly', not " + type);
        break;
    }
    console.log("Fetching json for ", type, " at ", url);
    return this.http.post<string[]>(`${url}`, data, { responseType: 'json', reportProgress: true, withCredentials: true });
  }

  get_meta(type: string, data?: Object): Observable<Fields> {
    let url: string = "";
    switch (type) {
      case 'epistack':
        url = this.build_url('epistack/filter', data);
        break;
      case 'fields':
        url = this.build_url('metadata/fields', data);
        break;
      case 'metadata':
        url = this.build_url('metadata/all', data);
        break;
      case 'table':
        url = this.build_url('metadata/table', data);
        break;
      default:
        throw new Error("Invalid parameter: type must be 'epistack', not " + type);
        break;
    }
    console.log("Fetching metadata for ", type, " at ", url);
    return this.http.get<Fields>(`${url}`, { responseType: 'json', reportProgress: true, withCredentials: true });
  }

  get_list(type: string, data?: Object): Observable<string[]> {
    let url: string = "";
    switch (type) {
      case 'epistack':
        url = this.build_url('epistack/imgs', data);
        break;
      case 'species':
        url = this.build_url('data/list/species');
        break;
      case 'experiments':
        url = this.build_url(`data/list/species/${data as string}`);
        break;
      default:
        throw new Error("Invalid parameter: type must be 'epistack' or 'species', not " + type);
        break;
    }
    console.log("Fetching list for ", type, " at ", url);
    return this.http.get<string[]>(`${url}`, { responseType: 'json', reportProgress: true, withCredentials: true });
  }

  get_json(type: string, data?: Object): Observable<Object> {
    let url: string = "";
    switch (type) {
      case 'plotly':
        url = this.build_url('heatmap/plotly', data);
        break;
      case 'legend':
        url = this.build_url('heatmap/legend');
        break;
      default:
        throw new Error("Invalid parameter: type must be 'plotly', not " + type);
        break;
    }
    console.log("Fetching json for ", type, " at ", url);
    return this.http.get<string[]>(`${url}`, { responseType: 'json', reportProgress: true, withCredentials: true });
  }

  get_blob(type: string, data?: Object): Observable<Blob> {
    let url: string = "";
    switch (type) {
      case 'heatmap':
        url = this.build_url('heatmap/img', data);
        break;
      default:
        throw new Error("Invalid parameter: type must be 'heatmap', not " + type);
    }
    console.log("Fetching blob for ", type, " at ", url);
    return this.http.get(`${url}`, { responseType: 'blob', reportProgress: true, withCredentials: true });
  }

  get_legend(): Observable<Object> {
    let url = `${this.baseURL}/api/legend`;
    console.log("Fetching legend at ", url);
    return this.http.get(url, { responseType: 'json', withCredentials: true })
  }

  submit_data(data: Object): void {
    this.submittedData.next(data);
  }

  filter_highlight(data: Object): Observable<Blob> {
    //    const sp = data['species'].replace(" ", "_");
    let url: string = `${this.baseURL}/api/img/`;
    console.log(data);
    url = url + `?q=${JSON.stringify(data)}`;
    console.log("Fetching image at ", url);
    //    return url;
    return this.http.get(`${url}`, { responseType: 'blob', reportProgress: true, withCredentials: true });
  }

  get_plotly(data: Object): Observable<Object> {
    //    const sp = data['species'].replace(" ", "_");
    let url: string = `${this.baseURL}/api/json/`;
    console.log(data);
    url = url + `?q=${JSON.stringify(data)}`;
    console.log("Fetching plotly at ", url);
    //    return url;
    return this.http.get(`${url}`, { responseType: 'json', reportProgress: true, withCredentials: true });
  }

  get_annotated_plotly(data: Object): Observable<Object> {
    //    const sp = data['species'].replace(" ", "_");
    let url: string = `${this.baseURL}/api/annotated_plotly/`;
    console.log(data);
    url = url + `?q=${JSON.stringify(data)}`;
    console.log("Fetching annotated plotly at ", url);
    //    return url;
    return this.http.get(`${url}`, { responseType: 'json', reportProgress: true, withCredentials: true });
  }

  get_fields(data: Object): Observable<Fields> {
    let url = `${this.baseURL}/api/fields/`;
    url = url + `?q=${JSON.stringify(data)}`;
    console.log("Fetching fields at ", url);
    return this.http.get<Fields>(url, { responseType: 'json' })
  }

  get_experiments(species: string): Observable<string[]> {
    let url = `${this.baseURL}/api/${species}/experiments`;
    console.log(`Fetching available experiments for ${species}`);
    return this.http.get<string[]>(url, { responseType: 'json' })
  }

  get_species(): Observable<string[]> {
    let url = `${this.baseURL}/api/species`;
    console.log(`Fetching available species`);
    return this.http.get<string[]>(url, { responseType: 'json' })
  }

  get_size(data: Object): Observable<string> {
    let url = `${this.baseURL}/api/size`;
    console.log(`Fetching size`);
    url = url + `?q=${JSON.stringify(data)}`;
    return this.http.get(url, { responseType: 'text' })
  }

  get_metadata(data: Object): Observable<Object> {
    let url = `${this.baseURL}/api/metadata`;
    url = url + `?q=${JSON.stringify(data)}`;
    console.log(`Fetching metadata at`, url);
    return this.http.get(url, { responseType: 'json' })
  }

  get_epistack_meta(data: object): Observable<Fields> {
    let url = `${this.baseURL}/api/epistack`;
    url = url + `?q=${JSON.stringify(data)}`;
    console.log("Fetching epistack metadata at ", url);
    return this.http.get<Fields>(url, { responseType: 'json' })
  }

  /*
  get(uri: string, response: string, data?:Object): Observable<string[]>;
  get(uri: string, response: string, data?:Object): Observable<Fields>;
  
  get(uri: string, response: string, data?: Object): Observable<any> {
    let url = `${this.baseURL}/${uri}`;
    if (typeof data !== "undefined") {
      url = url + `?q=${JSON.stringify(data)}`;
    }
    console.log("Fetching data at ", url);
    switch (response) {
      case 'blob':
        return this.http.get(`${url}`, {responseType: 'blob', reportProgress: true, withCredentials: true});
        break;
      default:
        return this.http.get(`${url}`, {responseType: 'json', reportProgress: true, withCredentials: true});
        break;
    }
  }
  
  get_epistack(type: string, data: Object): Observable<Fields>;
  get_epistack(type: string, data: Object): Observable<string[]>;
  
  get_epistack_meta(data: object): Observable<Fields> {
    let url = `${this.baseURL}/api/epistack`;
    url = url + `?q=${JSON.stringify(data)}`;
    console.log("Fetching epistack metadata at ", url);
    return this.http.get<Fields>(url, {responseType: 'json'})
  }
  
  get_epistack_img(data: object): Observable<string[]> {
    let url = `${this.baseURL}/api/epistack_imgs`;
    url = url + `?q=${JSON.stringify(data)}`;
    console.log("Fetching epistack image at ", url);
    return this.http.get<string[]>(`${url}`, {responseType: 'json', reportProgress: true, withCredentials: true});
  }
  */
}
