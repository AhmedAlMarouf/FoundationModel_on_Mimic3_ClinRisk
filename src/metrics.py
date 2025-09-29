from sklearn.metrics import roc_auc_score, average_precision_score, f1_score, brier_score_loss

def evaluate_all(y_true, proba, preds):
    return {
        "auroc": float(roc_auc_score(y_true, proba)),
        "auprc": float(average_precision_score(y_true, proba)),
        "f1": float(f1_score(y_true, preds)),
        "brier": float(brier_score_loss(y_true, proba)),
    }
