import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.css']
})
export class TestComponent implements OnInit {
  file:any;
  public loading: boolean = false;

  constructor(dataService: DataService) { }

  ngOnInit(): void { }

  fileChanged(e) {
      this.file = e.target.files[0];
  }

  onSubmit() {
    let fileReader = new FileReader();
    fileReader.onloadstart = (e) => {
      this.loading = true;
    }
    fileReader.onloadend = (e) => {
      this.loading = false;
      console.log(fileReader.result);
    }
    fileReader.readAsText(this.file);
  }




}
