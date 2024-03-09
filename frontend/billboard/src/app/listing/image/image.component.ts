import { Component } from '@angular/core';

@Component({
  selector: 'app-image',
  standalone: true,
  imports: [],
  templateUrl: './image.component.html',
  styleUrl: './image.component.scss'
})
export class ImageComponent {
  public imageURL = 'https://cdn.waterstones.com/bookjackets/large/9781/1084/9781108455145.jpg';
}
