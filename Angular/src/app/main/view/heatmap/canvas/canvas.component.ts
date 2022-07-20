import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { fromEvent } from 'rxjs';
import { HeatmapInfoService } from '../../../heatmap-info.service';


@Component({
  selector: 'app-canvas',
  templateUrl: './canvas.component.html',
  styleUrls: ['./canvas.component.css']
})
export class CanvasComponent implements OnInit {
  private img: HTMLImageElement = new Image();
  public hide: boolean;
  @ViewChild('canvas', {static: false}) canvas: ElementRef<HTMLCanvasElement>;

  public context: CanvasRenderingContext2D;

  constructor(private heatmapInfoService: HeatmapInfoService,) { }

  ngOnInit(): void {
    console.log("Canvas Init");
    this.hide = true;
    this.img.addEventListener("load", () => {
      this.draw_img()
    })
  }

  ngAfterViewInit(): void {
  }

  get_pixel_color(e): void {
    let x = e.pageX - this.canvas.nativeElement.offsetLeft;
    let y = e.pageY - this.canvas.nativeElement.offsetTop;

    let imgdata = this.context.getImageData(x, y, 1, 1);
    let pixel = imgdata.data;

    this.heatmapInfoService.pixel_color(`rgb(${pixel[0]}, ${pixel[1]}, ${pixel[2]})`);
  }

  setImg(src: string): void {
    console.log("Loading image for canvas");
    this.img = new Image();
    this.img.addEventListener("load", () => {
      console.log("Image loaded for canvas");
      this.draw_img()
    })
    //console.log("Source image for canvas: ", src);
    this.img.src = src;
  }

  draw_img(): void {
    //console.log("Canvas drawing image: ", this.img);
    //console.log(this.img);
    //console.log(this.img.src);
    //console.log(this.img.height, this.img.width);
    this.canvas.nativeElement.height = this.img.height;
    this.canvas.nativeElement.width = this.img.width;
    //this.canvas.style.height = this.img.height;
    //this.canvas.style.width = this.img.width;
    console.log(this.canvas);
    this.context = this.canvas.nativeElement.getContext('2d');
    this.context.drawImage(this.img, 0, 0);
    this.hide = false;
    let mousemove$ = fromEvent(this.canvas.nativeElement, 'mousemove');
    mousemove$.subscribe((event) => {
      this.get_pixel_color(event);
    })
  }


}
