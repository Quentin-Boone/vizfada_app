import { Component, HostListener, Directive, HostBinding, Input} from '@angular/core';

@Directive({selector: '[canvasDir]'})
export class HostDirective {
  @HostBinding('title') title = 'placeholder';
  @HostBinding('data-toggle')

  constructor(private elementRef: ElementRef){}
}
