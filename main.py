from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from typing import List

app = FastAPI()

# Dependência para pegar a sessão do banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para criar uma empresa
@app.post("/empresas/", response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = models.Empresa(nome=empresa.nome, cnpj=empresa.cnpj, endereco=empresa.endereco, 
                                email=empresa.email, telefone=empresa.telefone)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

# Endpoint para listar todas as empresas
@app.get("/empresas/", response_model=List[schemas.Empresa])
def get_empresas(db: Session = Depends(get_db)):
    return db.query(models.Empresa).all()

# Endpoint para criar uma obrigação acessória
@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoria)
def create_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = models.ObrigacaoAcessoria(nome=obrigacao.nome, periodicidade=obrigacao.periodicidade, 
                                            empresa_id=obrigacao.empresa_id)
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

# Endpoint para listar as obrigações acessórias de uma empresa
@app.get("/empresas/{empresa_id}/obrigacoes", response_model=List[schemas.ObrigacaoAcessoria])
def get_obrigacoes(empresa_id: int, db: Session = Depends(get_db)):
    return db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.empresa_id == empresa_id).all()
