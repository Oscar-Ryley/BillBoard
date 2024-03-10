import { Component } from '@angular/core';
import { FormsModule, NgForm } from '@angular/forms';
import { ApiService } from '../api.service';

type CreateOfferFormData = {
  bookID: number;
  price: number;
  condition: 'used' | 'new';
  notes: string | null;
  location: string;
  date: string;
  seller: { id: number; };
};

@Component({
  selector: 'app-create-offer',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './create-offer.component.html',
  styleUrl: './create-offer.component.scss'
})
export class CreateOfferComponent {
  public formData: any = {
    bookID: '',
    price: '',
    condition: '',
    notes: '',
    location: '',
    date: '',
    seller: ''
  };

  public conditions = [
    { name: 'New', value: 'new', selected: false },
    { name: 'Used', value: 'used', selected: false }
  ];

  constructor(private apiService: ApiService) {}

  submitForm(form: NgForm) {
    if (!form.valid) {
      console.log('uh oh');
    } else {
      this.formData.condition = this.conditions.find(c => c.selected)?.value!;
      this.formData.date = new Date().toISOString();
      this.formData.seller = { id: parseInt(this.formData.seller), username: 'Admin' };
      this.apiService.create(this.formData);
    }
  }
}
