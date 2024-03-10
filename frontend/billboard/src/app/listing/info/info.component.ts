import { Component, Input } from '@angular/core';
import { Listing } from '../../api.service';
import { CommonModule, CurrencyPipe } from '@angular/common';

@Component({
  selector: 'app-info',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './info.component.html',
  styleUrl: './info.component.scss'
})
export class InfoComponent {
  @Input() listing: Listing | undefined;
}
