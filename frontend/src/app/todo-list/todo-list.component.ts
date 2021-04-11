import { Component, OnInit } from '@angular/core';
import {ConfigService} from '../config.service';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit {

  constructor(
        private config: ConfigService
  ) { }

  todo_list: any;
  id: any;
  title: any;
  description: any;
  get_todo_list(): void {
    let response_data = this.config.Request('todo/', 'get');
    response_data.subscribe(
              res_data => {
                console.log("success!", res_data);
                this.todo_list = res_data;
              },
              error => {
                console.log("couldn't post because", error);
              }
          );
  }
  todo_show = false;
  todo_focus(selected=false): void {
    console.log("Focuesd");
    this.todo_show = selected;
  }

  todo_edit(item: any): void{
    this.id = item.id;
    this.title = item.title;
    this.description = item.description;
    this.todo_show = true;
  }
  close(): void {
    let data = {title: this.title, description: this.description}
    let data_id = 0;
    let method = 'post'
    if(this.id){
      method = 'put';
    }
    let response_data = this.config.Request('todo/', method, data, this.id);
    response_data.subscribe(
              res_data => {
                console.log("success!", res_data);
                this.todo_list = res_data;
                this.get_todo_list();
                this.todo_show = false;
                this.title = '';
                this.description = '';
                this.id = '';
              },
              error => {
                console.log("couldn't post because", error);
                this.todo_show = false;
              }
          );
  }

  todo_delete(data_id=0): void{
    let data = {};
    let response_data = this.config.Request('todo/', 'delete', data, data_id);
    response_data.subscribe(
              res_data => {
                console.log("success!", res_data);
                this.get_todo_list();
              },
              error => {
                console.log("couldn't post because", error);
              }
          );
  }


  ngOnInit(): void {
    this.get_todo_list();
  }


}
