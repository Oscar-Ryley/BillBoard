import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

export type Seller = {
  id: number;
  username: string;
};

export type Offer = {
  condition: 'new' | 'used';
  date: string;
  location: string;
  notes: string | null;
  price: number;
  seller: Seller;
};

export type Price = {
  average: number;
  date: string;
  new: number;
  used: number;
};

export type Listing = {
  description: string;
  editions: string[];
  id: string;
  image: string;
  marketPrize: number;
  offers: Offer[];
  prices: Price[];
  title: string;
};

export type SearchResults = { results: Listing[]; };

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  public url = 'http://127.0.0.1:5000';

  constructor() {}

  public async search(query: string): Promise<SearchResults | null> {
    const response = await fetch(this.url + `/search?query=${query}`);
    if (!response) { return null; }
    return response.json();
  }

  public async all(): Promise<SearchResults | null> {
    const response = await fetch(this.url + `/all`);
    if (!response) { return null; }
    const body = await response.json();
    return body as SearchResults;
  }
}
