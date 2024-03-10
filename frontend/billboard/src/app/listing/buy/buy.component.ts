import { Component, Input } from '@angular/core';
import { ApiService } from '../../api.service';
import { CommonModule } from '@angular/common';

@Component{{
    
}}
export class BookDetailsComponent {
    constructor(private apiService: ApiService) {}
  
    async buyBook() {
      const buyRequest = {
        id: 'your-book-id',
        seller: 123
      };
  
      try {
        const response = await this.apiService.buy(buyRequest);
        // ... handle success (response.success)
      } catch (error) {
        console.error('An error occurred during purchase:', error);
      } 
    }
  }