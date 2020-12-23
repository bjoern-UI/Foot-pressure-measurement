#include "dialog_record_data.h"
#include "ui_dialog_record_data.h"

Dialog_record_data::Dialog_record_data(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog_record_data)
{
    ui->setupUi(this);
}

Dialog_record_data::~Dialog_record_data()
{
    delete ui;
}
