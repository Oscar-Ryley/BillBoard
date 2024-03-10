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
  id: string;
  description: string;
  editions: string[];
  image: string;
  marketPrize: number;
  offers: Offer[];
  prices: Price[];
  title: string;
};

interface BuyRequest {
  id: string;
  seller: number;
}

interface BuyResponse {
  success: boolean;
}

export type SearchResults = { results: Listing[]; };

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  public url = 'http://127.0.0.1:5000';
  public listing: Listing | undefined;

  constructor() {}

  public async search(query: string): Promise<SearchResults | null> {
    const response = await fetch(this.url + `/search?query=${query}`);
    if (!response) { return null; }
    const body = await response.json();
    return body as SearchResults;
  }

  public async getById(id: string): Promise<Listing | null> {
    const response = await fetch(this.url + `/listing/${id}`);
    if (!response) { return null; }
    const body = await response.json();
    return body as Listing;
  }

  public async all(): Promise<SearchResults | null> {
    const response = await fetch(this.url + `/all`);
    if (!response) { return null; }
    const body = await response.json();
    return body as SearchResults;
  }

  public async buy(buyRequest: BuyRequest): Promise<BuyResponse | null> {
    const response = await fetch(this.url + '/buy', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(buyRequest)
    });

    if (!response.ok) {
      console.error("Book purchase failed:", response.status);
      return null;
    }

    const body = await response.json();
    return body as BuyResponse;
  }
}
