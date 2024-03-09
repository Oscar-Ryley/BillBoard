import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { ListingComponent } from "./listing/listing.component";
import { SearchComponent } from "./search/search.component";

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  imports: [CommonModule, RouterOutlet, ListingComponent, SearchComponent]
})
export class AppComponent {
  title = 'billboard';
}
