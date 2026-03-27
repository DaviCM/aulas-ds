// Irá executar um evento depois que a página estiver carregada
document.addEventListener("DOMContentLoaded", () => {
    // Declarando as constantes com os ids da modal
    const tabela = document.querySelector('table tbody');

    const modalElement = document.getElementById("usuarioModal");
    // Verifica se existe uma instância da modal, cria uma se não existir
    const usuarioModal = bootstrap.Modal.getOrCreateInstance(modalElement);

    const tituloModal = document.getElementById("tituloModal");

    const usuarioForm = document.getElementById("usuarioForm");

    const btnAdicionar = document.getElementById("btnAdicionar");
    const btnEditar = document.getElementById("btnEditar");
    const btnExcluir = document.getElementById("btnExcluir");
    
    const inputNome = document.getElementById("inputNome");
    const inputEmail = document.getElementById("inputEmail");
    const inputTelefone = document.getElementById("inputTelefone");
    const modalIndex = document.getElementById("usuarioId");
    
    // Abrir modal para adicionar um usuário
    btnAdicionar.addEventListener("click", () => {
        tituloModal.textContent = "Adicionar Usuário";
        // Faz um reset em todos os campos do formulário
        // Deixa eles em branco
        usuarioForm.reset();

        // MmodalIndex vem do campo oculto 'id' dentro do HTML
        modalIndex.value = "";
        usuarioModal.show();

    });
    

    // Salvar (Adcionar ou Editar) e = Evento
    usuarioForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const nome = (inputNome.value).trim();
        const email = (inputEmail.value).trim();
        const telefone = (inputTelefone.value).trim();
        const index = modalIndex.value;

        if (index === "") {
            adicionarUsuario(nome, email, telefone);
        }
        else {
            editarUsuario(index, nome, email, telefone);
        };

        // Irá fechar a modal ao fim das transações
        usuarioModal.hide();
    });


    // Adicionar nova linha à tabela
    function adicionarUsuario(nome, email, telefone) {
        const novaLinha = tabela.insertRow();
        // TODO: Conferir
        const novoId = tabela.rows.length;

        novaLinha.innerHTML = `
        <th scope="row">${novoId}</th>
        <td>${nome}</td>
        <td>${email}</td>
        <td>${telefone}</td>

        <td>
            <button href="#" class="btn btn-warning btn-editar" id="btnEditar">Editar Usuário</button>
            <button href="#" class="btn btn-danger btn-excluir" id="btnExcluir">Excluir Usuário</button>
        </td>`;
    };


    // Atualizar linha da tabela
    function editarUsuario(index, nome, email, telefone) {
        const linha = tabela.rows[index];
        // Iguala os valores da linha correta, indicada pelo index, aos valores passados como parâmetro
        // O funcionamento vai mudar, porque a linha (row) já existe
        linha.cells[1].textContent = nome;
        linha.cells[2].textContent = email;
        linha.cells[3].textContent = telefone;
    };


    // Eventos da tabela (editar e excluir), e = Evento
    tabela.addEventListener("click", (e) => {
        // Captura a linha mais próxima, que é a que foi clicada. tr = table row
        const linha = e.target.closest("tr");
        // Se não houver linha, retorna vazio
        if (! linha) return;
        // Captura o índice da linha clicada. Interpreta a tabela como uma array, e pega a posição da linha correta
        const index = Array.from(tabela.rows).indexOf(linha);
        
        // Chamando pela classe ao invés de adicionar listener no id
        if (e.target.classList.contains('btn-editar')) {
            tituloModal.textContent = "Editar Usuário";
            
            modalIndex.value = index;
            inputNome.value = linha.cells[1].textContent;
            inputEmail.value = linha.cells[2].textContent;
            inputTelefone.value = linha.cells[3].textContent;
            
            usuarioModal.show();
        };
        
        if (e.target.classList.contains('btn-excluir')) {
            const confirmar = confirm("em certeza que deseja excluir esse usuário?")
            
            if (confirmar === true) {
                linha.remove();
                atualizarIds();
            }
            else return;
        };


        // Atualizar os ids da lista ao criar ou excluir users
        function atualizarIds() {
            Array.from(tabela.rows).forEach((linha, i) => {
                // Posição 0: Id
                // Pega o valor da iteração (em que linha se encontra) e soma 1
                // Para saber o valor real
                linha.cells[0].textContent = i + 1;
            });
        };
    });
});




