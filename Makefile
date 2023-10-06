all:
	@echo "make install"
	@echo "    Instala las bibliotecas de Python que serán usadas con conda"
	@echo "make run"
	@echo "    Corre el programa, requiere de dos argumentos R y FILE."
	@echo "make clean"
	@echo "    Limpia y elimina los archivos generados por el proyecto."

install:
	@conda install --file requirements.txt

clean:
	@rm ./src/*.class > /dev/null || true
	@rm -rf __pycache__ 2> /dev/null || true
	@reset

run:
	@reset
	@cd src
	R=${R} FILE="examples/"${FILE} java -jar lib/processing-py.jar src/Voronoi.pyde


