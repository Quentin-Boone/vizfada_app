import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';

import { NgbCarouselConfig } from '@ng-bootstrap/ng-bootstrap';

import { EpistackService } from '../epistack.service';

@Component({
  selector: 'app-carousel',
  templateUrl: './carousel.component.html',
  styleUrls: ['./carousel.component.css'],
  providers: [NgbCarouselConfig],
  encapsulation: ViewEncapsulation.None
})
export class CarouselComponent implements OnInit {
  
  public images: string[];
  @Input() side: string;
  public selected: string;

  constructor(private config: NgbCarouselConfig,
              private epistackService: EpistackService) {
    config.showNavigationArrows = true;
    config.showNavigationIndicators = true;
    config.interval = 0;
  }

  ngOnInit(): void {
    console.log(this.side, "panel initiated");
    if (this.side == "left") {
      this.epistackService.leftImages$.subscribe(data => {this.images = data; this.selected = this.getExp(this.images[0])});
    } else if (this.side === "right") {
      this.epistackService.rightImages$.subscribe(data => {this.images = data; this.selected = this.getExp(this.images[0])});
    }
  }

  getExp(source: string): string {
    return source.split("/").pop().split(".png")[0];
  }

  onSlide(event): void {
    this.selected = event.current;
  }

}



