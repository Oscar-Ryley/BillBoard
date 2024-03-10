import { Component, Input } from '@angular/core';
import { Offer } from '../../api.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-offers',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './offers.component.html',
  styleUrl: './offers.component.scss'
})
export class OffersComponent {
  @Input() offers: Offer[] = [];
}
