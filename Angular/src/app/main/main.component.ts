import { Component, ViewChild, OnInit } from '@angular/core';

import { ViewComponent } from "./view/view.component";
import { ControllerComponent } from "./controller/controller.component";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  @ViewChild(ControllerComponent) controller: ControllerComponent;
  @ViewChild(ViewComponent) view: ViewComponent;

  constructor() { }

  ngOnInit(): void {
  }

}
