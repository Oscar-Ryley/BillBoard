import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './search.component.html',
  styleUrl: './search.component.scss'
})
export class SearchComponent {
  public query: string = '';

  constructor(private apiService: ApiService) {}

  public onKeyDown(event: KeyboardEvent) {
    if (event.code == 'Enter') {
      if (this.query.trim() !== '') {
        this.apiService.searchAndDisplay(this.query);
      }
    }
  }
}
