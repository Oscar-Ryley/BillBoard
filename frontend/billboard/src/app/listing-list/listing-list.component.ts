import { Component, OnInit } from '@angular/core';
import { ApiService, Listing } from '../api.service';

@Component({
  selector: 'app-listing-list',
  standalone: true,
  imports: [],
  templateUrl: './listing-list.component.html',
  styleUrl: './listing-list.component.scss'
})
export class ListingListComponent implements OnInit {
  public results: Listing[] | undefined;
  public all: boolean = true;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.all().then((data) => {
      this.results = data!.results;
    });
  }
}
