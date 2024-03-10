import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './search.component.html',
  styleUrl: './search.component.scss'
})
export class SearchComponent {
  public query: string = '';

  public onKeyDown(event: KeyboardEvent) {
    if (event.code == 'Enter') {
      if (this.query.trim() !== '') {
        console.log(this.query);
      }
    }
  }
}
