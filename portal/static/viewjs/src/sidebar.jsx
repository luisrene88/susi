var multi = $("#navegacion").kendoMultiSelect({
    dataTextField:'nombre',
    dataValueField:'id',
    dataSource:[
    ],
    change: function(){
        $('#selected').val('');
        this.dataSource.data([]);
        if(dataS){
            dataS.page(1);
        }
    }
}).data("kendoMultiSelect");

$(multi.input).on('keypress',function(e){
          e.preventDefault();
});

var SubcategoriaSide = React.createClass({
    getInitialState:function(){
        return {
            activo : false
        }
    },
    displayName: 'subcategoriaSide',
    reloadData: function(){
        if(dataS){
            //debugger;
            $("#search").val('');
            $('#selected').val(this.props.id);
            multi.dataSource.data([]);
            multi.dataSource.add({id:this.props.id, nombre:this.props.nombre});
            multi.value([this.props.id]);
            dataS.page(1);
            
        }
    },
    render: function() {
        return (
            
            	<li>
            	<a className="k-link {this.state.activo}" onClick={this.reloadData} id={this.props.id}>{this.props.nombre}</a>
            	</li>
            
        );
    }
});

var CategoriaSide = React.createClass({
    displayName: 'categoriaSide',
    getInitialState: function(){
    	return {
    		subcategorias : [],
    		cargado : false,
            desplegado : false
    	}
    },
    eachItem: function(sub, i){
    	return (
    		<SubcategoriaSide
    		id = {sub.id}
    		nombre = {sub.nombre}
    		/>
    		)
    },
    loadSubcategoria: function(){
    	//debugger;
    	var self = this;
    	var _id = this.props.index;
    	var _url = '/api/subcategoria/?categoria='+_id;
        if (!this.state.cargado){
        	Promise.resolve($.get(_url))
        	.then(function(result){
        		self.setState({
        			subcategorias : result,
                    cargado:true,
                    desplegado :true
        		});
        		$("#"+self.props.index+"cat").next().slideToggle();
        	})
        	.catch(function(e){
        		console.log(e);
        	});
        }else{
            this.setState({
                desplegado : true
                });
            $("#"+self.props.index+"cat").next().slideToggle();
        }


    },
    render: function() {
        return (
            	<li>
            		<a className="k-link" onClick={this.loadSubcategoria} id={this.props.index+"cat"}>{this.props.nombre}</a>
            		<ul>
            		{this.state.subcategorias.map(this.eachItem)}
            		</ul>
            	</li>
        );
    }
});

var SideBar = React.createClass({
	getInitialState: function(){
		return {
			categorias : [],
			mostrar:false
		}
	},
	componentWillMount:function() {
	     

	      var self = this;
	      var url = '/api/categoria';
	      Promise.resolve($.get(url))
	      .then(function(result){
	      	//debugger;
	      	self.setState({
	      		categorias : result
	      	});
	      	
	      })
	      .catch(function(er){
	      	console.log(er);
	      })


	},
	aechItem: function(item, i){
		//debugger;
		return(
			<CategoriaSide
			index={item.id}
			nombre={item.nombre}
			/>
			)
	},
    show: function(){
        //debugger;
        this.setState({
            mostrar : !this.state.mostrar
        })

        if(!this.state.mostrar){
            $('.side').css('display','none');
            $('.art').addClass('hd-20');
        }
        else{
            $('.side').css('display','flex');
            $('.art').removeClass('hd-20');

        }
    },
	render: function(){
		return (
			<div className="">
			
                <input type="checkbox" hidden='hidden' onClick={this.show} id="categorias"/>
                <input type="text" hidden='hidden' id="selected"/>
				<ul className="sidebar ed-menu nav-bar">	
				{
					this.state.categorias.map(this.aechItem)
				}
				</ul>
			</div>	
			)
	}
});



ReactDOM.render(<SideBar/>, document.getElementById('sidebar'));

    

multi.ul.addClass("hide-selected");
$("#navegacion option").prop("disabled", "disabled");