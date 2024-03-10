import { Component, OnInit } from '@angular/core';
import { ApiService, Listing } from '../api.service';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-listing-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './listing-list.component.html',
  styleUrl: './listing-list.component.scss'
})
export class ListingListComponent implements OnInit {
  public results: Listing[] | undefined;

  constructor(private apiService: ApiService, private router: Router) {}

  ngOnInit(): void {
    this.apiService.all().then((data) => {
      this.results = data!.results;
    });
  }

  showListing(listingId: string) {
    this.apiService.getById(listingId).then((data) => {
      this.apiService.listing = data!;
      this.router.navigate(['/listing']);
    });
  }
}
