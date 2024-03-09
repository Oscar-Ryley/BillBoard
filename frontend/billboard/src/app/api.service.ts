import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

type Listing = {

};

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  public url = 'http://127.0.0.1:5000';
  public listing: Listing | null = null;

  constructor(private http: HttpClient) {
  }
}
