import { Component } from '@angular/core';
import { InfoComponent } from './info/info.component';
import { ImageComponent } from "./image/image.component";
import { ListingListComponent } from "../listing-list/listing-list.component";
import { SalesHistoryComponent } from "./sales-history/sales-history.component";
import { ApiService } from '../api.service';

@Component({
  selector: 'app-listing',
  standalone: true,
  templateUrl: './listing.component.html',
  styleUrl: './listing.component.scss',
  imports: [InfoComponent, ImageComponent, ListingListComponent, SalesHistoryComponent]
})
export class ListingComponent {
  constructor(private apiService: ApiService) {}

  public get listing() {
    return this.apiService.listing;
  }
}
