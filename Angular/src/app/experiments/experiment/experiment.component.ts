import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataJSON, Folder } from '../../utils/text-url';
import { ExperimentService } from '../experiment.service';


@Component({
  selector: 'app-experiment',
  templateUrl: './experiment.component.html',
  styleUrls: ['./experiment.component.css']
})
export class ExperimentComponent implements OnInit {
    
  @Input() id: string;
  public file_list: DataJSON[];
  public htmls: string[];
  public selectedFile: DataJSON = {url: "", name: "", mtime:"", download: "", parent: "", size: 0, type:""};
  public tree: (DataJSON | Folder)[];
  public folders: Object[];
  
  objectKeys = Object.keys;
  
  constructor(private experimentService: ExperimentService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.id = this.route.snapshot.paramMap.get('id');
    this.experimentService.get_experiment(this.id).subscribe(data => {
      this.tree = data;
      this.folders = this.getFolders(data[this.id]);
      console.log("Folders:", this.folders);
    });
  }
  
  isFolder(file: any): file is Folder {
    return typeof(file.name) === "undefined";
  }
  
  getFolders(tree: Folder): Object[] {
    let folders = [];
    for (let [name, files] of Object.entries(tree)) {
      folders.push({"name": name, "expanded": false});
      if (this.isFolder(files)) {
        console.log("Files: ", files);
        folders.concat(this.getFolders(files));
      }
    }
    return folders;
  }
  
  selectFile(file: DataJSON): void {
    this.selectedFile = file;
  }
  
  offset(depth: number): string {
    return depth*10 + 'px';
  }

}
