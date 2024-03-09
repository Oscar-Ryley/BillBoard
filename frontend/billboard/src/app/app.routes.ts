import { Routes } from '@angular/router';
import { ListingComponent } from './listing/listing.component';
import { ListingListComponent } from './listing-list/listing-list.component';

export const routes: Routes = [
    { path: '', component: ListingListComponent },
    { path: 'listing', component: ListingComponent }
];
