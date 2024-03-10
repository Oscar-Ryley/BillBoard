import { Component, Input } from '@angular/core';
import { Price } from '../../api.service';

@Component({
  selector: 'app-sales-history',
  standalone: true,
  imports: [],
  templateUrl: './sales-history.component.html',
  styleUrl: './sales-history.component.scss'
})
export class SalesHistoryComponent {
  @Input() prices: Price[] = [
    {
      average: 40,
      date: "01/01/2024",
      new: 40,
      used: 40
    },
    {
      average: 26,
      date: "02/01/2024",
      new: 40,
      used: 40
    },
    {
      average: 33,
      date: "03/01/2024",
      new: 40,
      used: 40
    },
    {
      average: 19,
      date: "04/01/2024",
      new: 40,
      used: 40
    },
    {
      average: 51,
      date: "05/01/2024",
      new: 40,
      used: 40
    }
  ];

  public get x() {
    return this.prices.map(e => new Date(e.date));
  }

  public get y() {
    return this.prices.map(e => e.average);
  }

  public get xNorm() {
    return this.x.map((e, i) => `${(100 * i) / (this.x.length - 1)}%`);
  }

  public get yNorm() {
    const max = Math.max(...this.y);
    return this.y.map(e => `${100 - (100 * e / max)}%`);
  }

  public get normPoints() {
    return this.xNorm.map((e, i) => ({ x: e, y: this.yNorm[i] }));
  }

  public get lines() {
    const lines = [];
    for (let i = 0; i < this.normPoints.length - 1; i++) {
      lines.push({ x1: this.xNorm[i], y1: this.yNorm[i], x2: this.xNorm[i + 1], y2: this.yNorm[i + 1] });
    }
    return lines;
  }
}
