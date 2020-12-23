#include "dialog_evaluate_data.h"
#include "ui_dialog_evaluate_data.h"

Dialog_Evaluate_Data::Dialog_Evaluate_Data(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog_Evaluate_Data)
{
    ui->setupUi(this);
}

Dialog_Evaluate_Data::~Dialog_Evaluate_Data()
{
    delete ui;
}

void Dialog_Evaluate_Data::on_graphicsView_rubberBandChanged(const QRect &viewportRect, const QPointF &fromScenePoint, const QPointF &toScenePoint)
{

}
