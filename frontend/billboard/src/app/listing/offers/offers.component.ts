import { Component, Input } from '@angular/core';
import { ApiService, Offer } from '../../api.service';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-offers',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './offers.component.html',
  styleUrl: './offers.component.scss'
})
export class OffersComponent {
  @Input() offers: Offer[] = [];

  constructor(private apiService: ApiService, private router: Router) {}

  buy(offer: Offer) {
    // @ts-ignore
    this.apiService.buy({ id: this.apiService.listing.id, seller: offer.seller.id });
    this.router.navigate(['']);
  }
}
