#ifndef DIALOG_RECORD_DATA_H
#define DIALOG_RECORD_DATA_H

#include <QDialog>

namespace Ui {
class Dialog_record_data;
}

class Dialog_record_data : public QDialog
{
    Q_OBJECT

public:
    explicit Dialog_record_data(QWidget *parent = nullptr);
    ~Dialog_record_data();

private:
    Ui::Dialog_record_data *ui;
};

#endif // DIALOG_RECORD_DATA_H
