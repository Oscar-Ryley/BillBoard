import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

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
  public listing: Listing = {
    "description": "A balanced introduction to the three major areas of finance: institutions and markets, investments, and financial management.",
    "editions": [
      "1119561175"
    ],
    "id": "1119561175",
    "image": "https://m.media-amazon.com/images/I/71ihZf6-kcL._SL1500_.jpg",
    "marketPrize": 125.65,
    "offers": [
      {
        "condition": "used",
        "date": "Sat, 09 Mar 2024 16:49:32 GMT",
        "location": "Durham",
        "notes": null,
        "price": 44.95,
        "seller": {
          "id": 1,
          "username": "samjohnson"
        }
      },
      {
        "condition": "new",
        "date": "2021-01-01T12:00:00Z",
        "location": "Sheffield",
        "notes": null,
        "price": 49.99,
        "seller": {
          "id": 69,
          "username": "Erik"
        }
      }
    ],
    "prices": [
      {
        "average": 44.83,
        "date": "Sat, 09 Mar 2024 16:49:32 GMT",
        "new": 59.95,
        "used": 30.0
      }
    ],
    "title": "Introduction to Finance: Markets, Investments, and Financial Management"
  };

  public listingListSubject = new Subject<SearchResults>();

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

  public async create(data: any) {
    await fetch(this.url + '/create',
      {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'Content-Type': 'application/json'
        }
      });
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

  public searchAndDisplay(query: string) {
    this.search(query).then((data) => {
      this.listingListSubject.next(data!);
    });
  }
}
