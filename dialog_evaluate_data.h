#ifndef DIALOG_EVALUATE_DATA_H
#define DIALOG_EVALUATE_DATA_H

#include <QDialog>

namespace Ui {
class Dialog_Evaluate_Data;
}

class Dialog_Evaluate_Data : public QDialog
{
    Q_OBJECT

public:
    explicit Dialog_Evaluate_Data(QWidget *parent = nullptr);
    ~Dialog_Evaluate_Data();

private slots:
    void on_graphicsView_rubberBandChanged(const QRect &viewportRect, const QPointF &fromScenePoint, const QPointF &toScenePoint);

private:
    Ui::Dialog_Evaluate_Data *ui;
};

#endif // DIALOG_EVALUATE_DATA_H
